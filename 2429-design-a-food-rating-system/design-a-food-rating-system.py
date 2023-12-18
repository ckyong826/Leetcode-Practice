from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ratingDict={}
        self.cuisineDict={}
        self.mapDict=defaultdict(SortedList)
        for i in range(len(foods)):
            self.ratingDict[foods[i]]=ratings[i]
            self.cuisineDict[foods[i]]=cuisines[i]
            self.mapDict[cuisines[i]].add((-ratings[i],foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine,rate=self.cuisineDict[food],self.ratingDict[food]
        self.ratingDict[food]=newRating
        self.mapDict[cuisine].discard((-rate,food))
        self.mapDict[cuisine].add((-newRating,food))

    def highestRated(self, cuisine: str) -> str:
        return self.mapDict[cuisine][0][1]
            


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)