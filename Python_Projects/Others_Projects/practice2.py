class TagCloud:
    def __init__(self):
        self._tags = {}
    def add(self, tag):
        tag = tag.lower()
        self._tags[tag] = self._tags.get(tag, 0) + 1
    def __getitem__(self, tag):
        return self._tags.get(tag.lower(), 0)
    def __setitem__(self, tag, count):
        self._tags[tag.lower()] = count
    def __len__(self):
        return len(self._tags)

cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("AI")

print(cloud["python"])  
print(len(cloud))
cloud["python"] = 10    
print(cloud["python"])  

cloud["java"] = 3       
print(cloud["java"]) 