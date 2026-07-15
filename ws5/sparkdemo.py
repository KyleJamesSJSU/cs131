from pyspark.sql import SparkSession # Create a SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import RegressionEvaluator
import sys

# A1: create spark session named ws5-regression
spark = SparkSession.builder.appName("ws5-regression").getOrCreate()

# A2: read dataset without hardcoding, and show it
# get from variable
path = sys.argv[1]
# read it
df = (spark.read.format("csv")
    .option("inferSchema", "true") # Infer schema (data types)
    .option("header", "true")
    .load(path))
# show it
df.show()

# A3: combine "total_bill" and "size" into a vector column called "features"
vecAssembler = VectorAssembler(inputCols=["total_bill","size"],outputCol="features")
vecDF = vecAssembler.transform(df)
vecDF.select("total_bill","size","features","tip").show(10)

# A4: split data 80/20 train/test
trainDF, testDF = df.randomSplit([.8, .2], seed=123)
# TODO put print?

# A5: define LinearRegression, fit the model, then chain with A3 into pipeline
lr = LinearRegression(featuresCol="features",labelCol="tip")
# pipeline
pipeline = Pipeline(stages=[vecAssembler, lr])
pipelineModel = pipeline.fit(trainDF)

# A6: apply to test set to produce predictions
predDF = pipelineModel.transform(testDF)
predDF.select("total_bill","size","features","tip","prediction").show(10)

# A7: RMSE and R^2
regressionEvaluator = RegressionEvaluator(
    predictionCol="prediction",
    labelCol="tip")
# RMSE
rmse = regressionEvaluator.evaluate(predDF, {regressionEvaluator.metricName: "rmse"})
# R^2
r2 = regressionEvaluator.evaluate(predDF, {regressionEvaluator.metricName: "r2"})

# A8: pull lr out of pipeline, print coefficients & intercept, print RMSE and R^2
# pull
lrModel = pipelineModel.stages[-1]
# print coefficients and intercept
m = round(lrModel.coefficients[0], 2)
b = round(lrModel.intercept, 2)
print(f"Coefficients: {lrModel.coefficients}")
print(f"Intercept: {lrModel.intercept}")
print(f"Line formula: {m}x + {b}\n")
# print RMSE
print(f"RMSE: {rmse}")
# print R^2
print(f"R^2: {r2}")


