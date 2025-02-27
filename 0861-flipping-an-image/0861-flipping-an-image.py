class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for r in range(len(image)):
            for c in range((len(image) +  1) // 2):
                image[r][c], image[r][len(image) - c - 1] = image[r][len(image) - c - 1] ^ 1, image[r][c] ^ 1

        return image



