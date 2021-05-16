from pprint import pprint


class DataModelSchema:
    def __init__(self, raw_data) -> None:
        self.compatibility_level = raw_data['compatibilityLevel']
        self.created_timestamp = raw_data['createdTimestamp']
        self.last_processed = raw_data['lastProcessed']
        self.last_schema_update = raw_data['lastSchemaUpdate']
        self.last_update = raw_data['lastUpdate']
        self.model = Model(raw_data['model'])

    
class Model:
    def __init__(self, raw_data) -> None:
        self.annotations = raw_data['annotations']
        self.culture = raw_data['culture']
        self.cultures = raw_data['cultures']
        self.data_access_options = raw_data['dataAccessOptions']
        self.default_powerbi_data_source_version = raw_data['defaultPowerBIDataSourceVersion']
        self.modified_time = raw_data['modifiedTime']
        self.relationships = raw_data['relationships']
        self.source_query_culture = raw_data['sourceQueryCulture']
        self.structure_modified_time = raw_data['structureModifiedTime']
        self.tables = [Table(x) for x in raw_data['tables']]


class Table:
    def __init__(self, raw_data) -> None:
        self.annotations = raw_data['annotations']
        self.columns = raw_data['columns']
        self.hierarchies = raw_data.get('hierarchies')
        self.is_hidden = raw_data.get('isHidden')
        self.is_private = raw_data.get('isPrivate')
        self.lineage_tag = raw_data['lineageTag']
        self.name = raw_data['name']
        self.partitions = raw_data['partitions']
        self.structured_modified_time = raw_data['structureModifiedTime']