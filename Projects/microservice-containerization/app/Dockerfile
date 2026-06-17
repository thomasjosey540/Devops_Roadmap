# App image: build the Java app with Maven, run it on Tomcat.
# Multi-stage build keeps the final image slim.

# ---- Build stage ----
FROM maven:3.9-eclipse-temurin-17 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn -q dependency:go-offline
COPY src ./src
RUN mvn -q clean package -DskipTests

# ---- Runtime stage ----
FROM tomcat:10-jdk17-temurin
# Remove default Tomcat apps
RUN rm -rf /usr/local/tomcat/webapps/*
# Deploy the built WAR as ROOT
COPY --from=build /app/target/*.war /usr/local/tomcat/webapps/ROOT.war
EXPOSE 8080
CMD ["catalina.sh", "run"]