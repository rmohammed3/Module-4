# Create a collection of authors and the year they died
authors = {
    "Charles Dickens": 1870,
    "William Thackeray": 1863,
    "Anthony Trollope": 1882,
    "Gerard Manley Hopkins": 1889
}

# Print in the format: Charles Dickens died in 1870.
for author, date in authors.items():
    print(f"{author} died in {date}.")