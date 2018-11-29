from instance.db_config import connection

incidents = []

class IncidentModel():
    """Create incident model"""

    def __init__(self):
        self.db = connection()

    def create_incident_database(self):

        try:
            # cursor
            cur =  self.db.cursor()
            queries = (
                        """
            CREATE TYPE type AS ENUM ('redflag','incident')
        """,
        """
            CREATE TYPE current_status AS ENUM('draft', 'under investigation','resolved', 'rejected')
        """,
        """
            CREATE TABLE IF NOT EXISTS incident (
                incident_id SERIAL PRIMARY KEY NO NULL,
                created_on TIMESTAMP DEFAULT now() NOT NULL,
                created_by INT NOT NULL,
                type type,
                location VARCHAR(50),
                status current_status,
                image BYTEA,
                video BYTEA,
                comment VARCHAR(255),
                FOREIGN KEY (created_by)
                    REFERENCES user(user_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """
            )
            # execute
            for query in queries:
                cur.execute(query)
            cur.commit()

        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db is not None:
                self.db.close()

    def get_all_incident(self):
        # cursor
        cur = self.db.close()
        # execute
        cur.execute("SELECT * FROM incident")
        # fetch one
        data = cur.fetchall()
        for datum in enumerate(data):
            incidents.append(datum)
        return incidents

    def save_incident(self,type,location,status,image,video,comment):
        payload = {
            'type': type,
            'location':location,
            'status':status,
            'image': image,
            'video': video,
            'comment':comment
        }

        query = "INSERT INTO incident (type,location,status,image,video,comment) VALUES(%(type)s,%(location)s,%(status)s,%(image)s,%(video)s,$(comment)s)"

        cur = self.db.cursor()
        cur.execute(query,payload)
        self.db.commit()
        return payload