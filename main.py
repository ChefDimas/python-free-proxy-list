import scrape


def write_list_to_txt(mylist, filename="ips_list.txt"):
    with open(filename, 'w') as file:
        for item in mylist:
            file.write(f"{item}\n")


ls = scrape.Scrape()
write_list_to_txt(ls.scrape())
