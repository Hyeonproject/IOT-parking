<%--
  Created by IntelliJ IDEA.
  User: Hyeon
  Date: 2019-12-15
  Time: 오전 1:33
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
  <meta charset="utf-8">
  <title>What the Parking</title>
  <link href="css/bootstrap.min.css" rel="stylesheet">
  <script src="js/bootstrap.min.js"></script>
</head>
<body>
<div class="container">
  <h1>What the Parking</h1>
  <ul class="nav nav-pills">
    <li role="presentation" class="active"><a href="index.jsp">주의 주차장 전체 현황</a></li>
    <li role="presentation"><a href="KakaoMaps.html">주차장을 통한 데이터 분석</a></li>
  </ul>
</div>
<div class="container" id="map" style="width: 80%; height: 80%;"></div>
<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=d7aa1f48cb081dfe6bdc2e9c4e7beb61&libraries=services"></script>
<script>
  // 마커를 클릭하면 장소명을 표출할 인포윈도우 입니다
  var infowindow = new kakao.maps.InfoWindow({zIndex:1});

  var mapContainer = document.getElementById('map'), // 지도를 표시할 div
          mapOption = {
            center: new kakao.maps.LatLng(35.156565, 129.058205), // 지도의 중심좌표
            level: 2 // 지도의 확대 레벨
          };

  // 지도를 생성합니다
  var map = new kakao.maps.Map(mapContainer, mapOption);

  // 장소 검색 객체를 생성합니다
  var ps = new kakao.maps.services.Places(map);

  // 카테고리로 은행을 검색합니다
  ps.categorySearch('PK6', placesSearchCB, {useMapBounds:true});

  // 키워드 검색 완료 시 호출되는 콜백함수 입니다
  function placesSearchCB (data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {
      for (var i=0; i<data.length; i++) {
        displayMarker(data[i]);
      }
    }
  }

  // 지도에 마커를 표시하는 함수입니다
  function displayMarker(place) {
    // 마커를 생성하고 지도에 표시합니다
    var marker = new kakao.maps.Marker({
      map: map,
      position: new kakao.maps.LatLng(place.y, place.x)
    });

    // 마커에 클릭이벤트를 등록합니다
    kakao.maps.event.addListener(marker, 'click', function() {
      // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
      infowindow.setContent('<div style="padding:5px;font-size:12px;"><a href="op/parking1"> '
              + place.place_name + '</a></div>');
      infowindow.open(map, marker);
    });
  }

  var imageSrc = 'http://localhost:8080/resource/me.png', // 마커이미지의 주소입니다
          imageSize = new kakao.maps.Size(64, 69), // 마커이미지의 크기입니다
          imageOption = {offset: new kakao.maps.Point(27, 69)}; // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다.

  // 마커의 이미지정보를 가지고 있는 마커이미지를 생성합니다
  var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption),
          markerPosition = new kakao.maps.LatLng(35.156624, 129.058143); // 마커가 표시될 위치입니다

  // 마커를 생성합니다
  var marker = new kakao.maps.Marker({
    position: markerPosition,
    image: markerImage // 마커이미지 설정
  });

  // 마커가 지도 위에 표시되도록 설정합니다
  marker.setMap(map);
</script>
</body>
</html>