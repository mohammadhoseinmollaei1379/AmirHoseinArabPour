class TagCloud:
    def __init__(self):
        self.tags = {}
    def add(self, tag):
        tag = tag.lower()
        self.tags[tag] = self.tags.get(tag, 0) + 1
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("AI")

print(cloud.tags)
print(cloud["python"])  
print(cloud["ai"])      
print(cloud["java"]) 