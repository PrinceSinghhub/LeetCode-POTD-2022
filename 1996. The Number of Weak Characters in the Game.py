class Solution:
    def numberOfWeakCharacters(self, properties):

        properties.sort(key=lambda x: (-x[0], x[1]))

        print(properties)
        count = 0

        maxAttack = properties[0][0]
        maxDiff = properties[0][1]

        for i in range(1, len(properties)):

            if properties[i][0] < maxAttack and properties[i][1] < maxDiff:
                count += 1

            else:
                maxAttack = properties[i][0]
                maxDiff = properties[i][1]

        return count