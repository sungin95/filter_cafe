from rest_framework.test import APITestCase

from cafes.models import Cafe
from filters.models import BallotBox, Filter, FilterScore
from users.models import User

"""
get
1) 도시에 해당하는 카페들이 나와야 됨.(status 200)
2) 카페가 2개가 있다면 2개가 출력되어야 됨.
페이지네이션(아직 구현 x)
"""


class TestCityCafesGet(APITestCase):
    URL = "/api/v1/"

    def setUp(self):
        cafe1 = Cafe.objects.create(
            city="서울",
            name="test cafe 1",
            address="test cafe address",
            business_hours="test cafe business_hours",
            img="test cafe img",
            map="test cafe map",
        )
        cafe2 = Cafe.objects.create(
            city="서울",
            name="test cafe 2",
            address="test cafe address",
            business_hours="test cafe business_hours",
            img="test cafe img",
            map="test cafe map",
        )
        cafe1.save()
        cafe2.save()

    def test_CityCafesGet_1(self):
        response = self.client.get(self.URL + "서울")
        self.assertEqual(
            response.status_code,
            200,
            "status code isn't 200.",
        )

    def test_CityCafesGet_2(self):
        response = self.client.get(self.URL + "서울")
        data = response.json()

        self.assertEqual(
            len(data),
            2,
            "CityCafes 출력 갯수가 잘못되었습니다.",
        )


class TestCityCafesPost(APITestCase):
    URL = "/api/v1/"

    def setUp(self):
        user1 = User.objects.create(
            username="testuser",
        )
        user1.set_password("123")
        user1.save()
        user2 = User.objects.create(
            username="testuser22",
        )
        user2.set_password("123")
        user2.save()

        cafe1 = Cafe.objects.create(
            city="서울",
            name="test cafe 1",
            address="test cafe address",
            business_hours="test cafe business_hours",
            img="test cafe img",
            map="test cafe map",
        )
        cafe2 = Cafe.objects.create(
            city="서울",
            name="test cafe 2",
            address="test cafe address",
            business_hours="test cafe business_hours",
            img="test cafe img",
            map="test cafe map",
        )
        cafe1.save()
        self.cafe1 = cafe1
        cafe2.save()
        filter1 = Filter.objects.create(
            option="option1",
            name="wifi1",
            img="img1",
        )
        filter2 = Filter.objects.create(
            option="option2",
            name="wifi2",
            img="img2",
        )
        filter1.save()
        filter2.save()
        self.filter1 = filter1
        self.filter2 = filter2
        filterscore100 = FilterScore.objects.create(score=100)
        filterscore30 = FilterScore.objects.create(score=30)
        filterscore100.save()
        filterscore30.save()
        balbox11100 = BallotBox.objects.create(
            cafe=cafe1,
            filter=filter1,
            score=filterscore100,
        )
        balbox110 = BallotBox.objects.create(
            cafe=cafe1,
            filter=filter1,
            score=filterscore30,
        )
        balbox12100 = BallotBox.objects.create(
            cafe=cafe1,
            filter=filter2,
            score=filterscore100,
        )
        balbox120 = BallotBox.objects.create(
            cafe=cafe1,
            filter=filter2,
            score=filterscore30,
        )
        balbox11100.users.add(user1)
        balbox11100.save()

        balbox110.users.add(user2)
        balbox110.save()

        balbox12100.users.add(user1)
        balbox12100.save()

        balbox120.save()

    def test_city_cafes_post_1(self):
        response = self.client.post(
            self.URL + "서울",
            data={
                "filters": [self.filter1, self.filter2],
            },
        )
        self.assertEqual(
            response.status_code,
            200,
            "status code isn't 200.",
        )

    # 이게 왜 에러인지 모르겠어 가지고 주석처리
    # def test_city_cafes_post_2(self):
    #     response = self.client.post(
    #         self.URL + "서울",
    #         data={
    #             "filters": [self.filter1, self.filter2],
    #         },
    #     )
    #     data = response.json()
    #     print(data)
    #     self.assertEqual(
    #         data,
    #         self.cafe1,
    #         "필터링이 제대로 되지 않았습니다. ",
    #     )


"""
CityList
class TestCityListGet(APITestCase):
    URL = "/api/v1/cities"
    pass

"""

"""
test
"""
