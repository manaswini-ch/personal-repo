from pyspark.sql import SparkSession
def dataSchemaDF(dataDF,schema):
	spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
	df = spark.createDataFrame(data = dataDF, schema = schema)
	df.printSchema()