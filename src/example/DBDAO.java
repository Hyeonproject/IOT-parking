package example;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

public class DBDAO extends DBConnect {

    private DBDAO() { }

    private static DBDAO instance = new DBDAO();

    public static DBDAO getInstance() {
        return instance;
    }

    public ArrayList<ParkingBean> getall() {
        String sql = "select * from wtp_parking";
        ArrayList<ParkingBean> list = new ArrayList<ParkingBean>();
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        try {
            conn = DBConnect.connect();
            pstmt = conn.prepareStatement(sql);
            rs = pstmt.executeQuery();
            while (rs.next()) {
                ParkingBean parkingBean = new ParkingBean();
                parkingBean.setParking_no(rs.getString("parking_no"));
                parkingBean.setA1(rs.getString("A1"));
                parkingBean.setA2(rs.getString("A2"));
                parkingBean.setA3(rs.getString("A3"));
                parkingBean.setA4(rs.getString("A4"));
                parkingBean.setA5(rs.getString("A5"));
                parkingBean.setA6(rs.getString("A6"));
                parkingBean.setA7(rs.getString("A7"));
                parkingBean.setA8(rs.getString("A8"));
                parkingBean.setA9(rs.getString("A9"));
                parkingBean.setA10(rs.getString("A10"));
                list.add(parkingBean);
                for (int i = 0; i < list.size(); i++) {
                    System.out.println(list.get(i).getA1());
                }

            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (rs != null)
                    rs.close();
                if (pstmt != null)
                    pstmt.close();
                if (conn != null)
                    conn.close();
            } catch (Exception e) {
                e.printStackTrace();
            }

        }
        return list;
    }
}






