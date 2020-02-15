class Cosco_api_designRouter(object):
    """
    A router to control all database operations on models in
    the myapp2 application
    """
 
    def db_for_read(self, model, **hints):
        """
        Point all operations on Cosco_api_design models to 'Cosco_Shipment_db'
        """
        if model._meta.app_label == 'Cosco_api_design':
            return 'Cosco_Shipment_db'
        return None
 
    def db_for_write(self, model, **hints):
        """
        Point all operations on myapp models to 'other'
        """
        if model._meta.app_label == 'Cosco_api_design':
            return 'Cosco_Shipment_db'
        return None
 
    def allow_syncdb(self, db, model):
        """
        Make sure the 'Cosco_api_design' app only appears on the 'other' db
        """
        if db == 'Cosco_Shipment_db':
            return model._meta.app_label == 'Cosco_api_design'
        elif model._meta.app_label == 'Cosco_api_design':
            return False
        return None