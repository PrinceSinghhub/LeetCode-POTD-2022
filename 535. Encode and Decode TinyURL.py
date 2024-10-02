class Codec:

    def encode(self, longUrl):
        return longUrl
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """

    def decode(self, shortUrl):
        return shortUrl
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

ans = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
print(ans.decode(url))