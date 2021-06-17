### Task 5.6

#Implement a Pagination class helpful to arrange text on pages and list content on given page.
#The class should take in a text and a positive integer which indicate how many symbols will be allowed per each page (take spaces into account as well).
#You need to be able to get the amount of whole symbols in text, get a number of pages that came out and method that accepts the page number and return quantity of symbols on this page.
#If the provided page’s number is missing print the warning message "Invalid index. Page is missing". If you're familiar with Exceptions using in Python display the error message in this way.
#Pages indexing starts with 0.

#Example:
#```python
#>>> pages = Pagination('Your beautiful text', 5)
#>>> pages.page_count
#4
#>>> pages.item_count
#19

#>>> pages.count_items_on_page(0)
#5
#>>> pages.count_items_on_page(3)
#4
#>>> pages.count_items_on_page(4)
#Exception: Invalid index. Page is missing.
#```
#Optional: implement querying pages by symbols/words and displaying pages with all the symbols on it.
#If you're querying by symbol that appears on many pages or if your are querying by the word that is divided in two return an array of all the occurrences.

#Example:
#```python
#>>> pages.find_page('Your')
#[0]
#>>> pages.find_page('e')
#[1, 3]
#>>> pages.find_page('beautiful')
#[1, 2]
#>>> pages.find_page('great')
#Exception: 'Great' is missing on the pages
#>>> pages.display_page(0)
#'Your '
#>>> pages.count\_items\_on_page(4)
#Exception: Invalid index. Page is missing.
#```

class Paginator:
    def __init__(self, content, page_sz):
        self.page_sz = page_sz if page_sz > 0 else 0
        self.content = content
        self.__split_content()

    def get_sz_content(self):
        return len(self.content)

    def __split_content(self):
        self.pages = []
        page_all_sz = self.get_sz_content()
        begin = 0
        if not self.page_sz:
            self.pages.append((begin, page_all_sz - 1))
        else:
            while page_all_sz > 0:
                cur_page_sz = min(self.page_sz, page_all_sz)
                cur_page_end = begin + cur_page_sz
                self.pages.append((begin, cur_page_end))
                begin = cur_page_end
                page_all_sz -= cur_page_sz

    def get_pages_cnt(self):
        return len(self.pages)
    
    def __if_page_exists(self, page_num):
        if page_num >= self.get_pages_cnt():
            raise Exception('Invalid index. Page is missing.')

    def count_items_on_page(self, page_num):
        self.__if_page_exists(page_num)
        page = self.pages[page_num]
        return page[1] - page[0]

    def display_page(self, page_num):
        self.__if_page_exists(page_num)
        page = self.pages[page_num]
        begin, end = page[0], page[1]
        return self.content[begin:end]
    
    def find_page(self, text):
        res_pages = []
        for i, page in enumerate(self.pages):
            begin, end = page[0], page[1]
            if text in self.content[begin:end]:
                res_pages.append(i)
        return res_pages


if __name__=='__main__':
    txt = '''Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium,
           totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt,
           explicabo. nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur
           magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia
           dolor sit, amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt, ut labore et
           dolore magnam aliquam quaerat voluptatem. ut enim ad minima veniam, quis nostrum exercitationem ullam corporis
           suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? quis autem vel eum iure reprehenderit, qui in 
           ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?'''
    
    p = Paginator(txt, 50)
    print(p.pages)
    print('Pages count:', p.get_pages_cnt())
    print(p.count_items_on_page(0))
    print(p.display_page(0))
    print(p.find_page('ut'))
    #[0, 27, 28, 52, 57, 67, 71]
    print(p.display_page(15))
