package example;

import java.sql.*;
import java.util.ArrayList;

public class DBConnect {
    public static final String databaseDriver =  "com.mysql.cj.jdbc.Driver";
    public static final String databaseUrl = "jdbc:mysql://52.79.239.76:3306/wtp_test?serverTimezone=UTC";
    public static final String databaseUser = "LEE";
    public static final String databasePassword = "oradb";
    public static PreparedStatement preparedStatement;
    public static ResultSet resultSet;
    public static Connection connection = null;

    public static void main(String[] args) {
//        /* Connection TEST
        connect();
        // Close TEST
        close();

    }

    public static Connection connect() { //DB CONNECT
        try {
            Class.forName(databaseDriver);
            connection = DriverManager.getConnection(databaseUrl, databaseUser, databasePassword);
            if (connection != null) System.out.println("Connection Succeed");
            else System.out.println("Connection Failed");
        } catch (Exception e) {
            System.err.println("Connection Error! : " + e.getMessage());
            e.printStackTrace();
        }
        return connection;
    }

    public static void close() { //DB USE AFTER CLOSE
        try {
            if (connection != null) {
                connection.close();
            }
        } catch (SQLException e) {
            System.err.println("Connection Closing Failed! : " + e.getMessage());
            e.printStackTrace();
        }
    }
}