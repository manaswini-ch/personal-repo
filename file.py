from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from file2 import *
def schemaCreator(dataDF):
	schema = StructType([
			StructField('name', StructType([
				 StructField('firstname', StringType(), True),
				 StructField('middlename', StringType(), True),
				 StructField('lastname', StringType(), True)
				 ])),
			 StructField('dob', StringType(), True),
			 StructField('gender', StringType(), True),
			 StructField('gender', IntegerType(), True)
			 ])
	
	dataSchemaDF(dataDF,schema)
