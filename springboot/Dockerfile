# Step 1: Base image with Java
FROM openjdk:17-jdk-slim AS build

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy the build artifact (JAR file)
COPY target/userservice-0.0.1-SNAPSHOT.jar /app/userservice.jar

# Step 4: Expose the port your app will run on
EXPOSE 8080

# Step 5: Run the application
ENTRYPOINT ["java", "-jar", "userservice.jar"]
