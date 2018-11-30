import psycopg2
from instance.db_config import connection

incidents = []

class IncidentModel():
    """Create incident model"""

    def __init__(self):
        self.db = connection()


    def get_all_incidents(self):
        # cursor
        cur = self.db.cursor()
        # execute
        cur.execute("SELECT * FROM incidents")
        # fetch one
        data = cur.fetchall()
        for datum in enumerate(data):
            incidents.append(datum)
        return incidents

    def save_incident(self,type,location,status,image,video,comment):
        payload = {
            'type': redflag_type,
            'location':location,
            'status':status,
            'image': image,
            'video': video,
            'comment':comment
        }

        query = """INSERT INTO incidents (type,location,status,image,video,comment) VALUES(%(redflag_type)s,%(location)s,%(status)s,%(image)s,%(video)s,%(comment)s);"""
        cur = self.db.cursor()
        cur.execute(query,(payload))
        self.db.commit()
        return payload