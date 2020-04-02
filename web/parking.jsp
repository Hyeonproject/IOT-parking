<%--
  Created by IntelliJ IDEA.
  User: hyeon
  Date: 2019-12-19
  Time: 오전 1:56
  To change this template use File | Settings | File Templates.
  이 화면에서는 지도와 관련된 부분을 session으로 넘겨서 정보를 다음 지도 api에 관련된 정보를 정리해서 출력해주는
  뷰이다.
--%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>

<html>
<head>
    <title>What The Parking</title>
    <link href="${pageContext.request.contextPath}/css/bootstrap.min.css" rel="stylesheet">
    <script src="${pageContext.request.contextPath}/js/bootstrap.min.js"></script>

</head>
<body>
    <c:set var = "count" value ="0"/>
    <h1 class="container">What the Parking</h1>
    <div class="container">
        주차장 현항 :<br>
        <table class="table" border="1">
            <thead>
                <tr>
                    <th>1번구역</th>
                    <th>2번구역</th>
                    <th>3번구역</th>
                </tr>
            </thead>
            <tbody>
        <c:forEach var="list" items="${parkingbeans}">
            <%-- ${list.parking_no} ${list.a1} ${list.a2} ${list.a3} --%>
                <td>
                <fmt:parseNumber value="${list.a1}" var="a1N"/>
                <c:if test="${a1N eq 0}">
                    <c:out value="차량없음"/>
                </c:if>
                <c:if test="${a1N eq 1}">
                    <c:out value="차량있음"/>
                </c:if>
                </td>
                <td>
                <fmt:parseNumber value="${list.a2}" var="a2N"/>
                <c:if test="${a2N eq 0}">
                    <c:out value="차량없음"/>
                </c:if>
                <c:if test="${a2N eq 1}">
                    <c:out value="차량있음"/>
                </c:if>
                </td>
                <td>
                <fmt:parseNumber value="${list.a3}" var="a3N"/>
                <c:if test="${a3N eq 0}">
                    <c:out value="차량없음"/>
                </c:if>
                <c:if test="${a3N eq 1}">
                    <c:out value="차량있음"/>
                </c:if>
                </td>
            <c:set var="count" value="${count + a1N + a2N + a3N}"/>
        </c:forEach>
            </tbody>
        </table>
        <div class="container">
        사용중 : <c:out value="${count}"/> <br>
        <c:set var="notCount" value="${3 - a1N - a2N -a3N}"/>
        빈자리 : <c:out value="${notCount}"/>
        </div>
    </div>
</body>
</html>
