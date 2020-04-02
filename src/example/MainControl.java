package example;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.util.ArrayList;

//@WebServlet(name = "MainControl")
public class MainControl extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        //1. init
        HttpSession session = request.getSession(); //세션 객체 불러오기

        //2. dispatch request to processing component
        String pathInfo = request.getPathInfo();
        String viewName = "index.jsp"; //에러 뜨면 바로 보내게 하지만 나는 메인 페이지로 보내게

        if(pathInfo.equals("/parking1")){
            DBDAO dbdao = DBDAO.getInstance();
            ArrayList<ParkingBean> parkingbeans = dbdao.getall();
            for (int i = 0; i < parkingbeans.size(); i++) {
                System.out.println(parkingbeans.get(i).getA1());
            }
            request.setAttribute("parkingbeans",parkingbeans);
            viewName = "parking.jsp";
        }
        else if (pathInfo.equals("/parking2")){
            DBDAO dbdao = DBDAO.getInstance();
            ArrayList<ParkingBean> parkingbeans = dbdao.getall();
            session.setAttribute("parkingbeans",parkingbeans);
            viewName = "parking2.jsp";
        }

        //3. forward to view componet
        StringBuilder sb = new StringBuilder(viewName);
        sb.insert(0,"../");
        RequestDispatcher view = request.getRequestDispatcher(sb.toString());
        view.forward(request,response);
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doPost(request,response);
    }
}
