#!/usr/bin/python3

import random
import string


class HtmlGenerator:
    html_answer = ''

    def random_html(self):
        yield '<html><body>'
        yield '<body>'
        yield self.random_body()
        yield '</body></html>'

    def random_body(self):
        yield self.random_section()
        if random.randrange(2) == 0:
            yield self.random_body()

    def random_section(self):
        yield '<h1>'
        yield self.random_sentence()
        yield '</h1>'
        sentences = random.randrange(10, 20)
        for _ in range(sentences):
            yield self.random_sentence()

    def random_sentence(self):
        words = random.randrange(30, 40)
        yield (' '.join(self.random_word() for _ in range(words)) + '.').capitalize()

    def random_word(self):
        chars = random.randrange(2, 10)
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(chars))

    def output(self, generator):
        if isinstance(generator, str):
            self.html_answer = self.html_answer + generator + '\n'
        else:
            for g in generator:
                self.output(g)

    def get_html(self):
        self.output(self.random_html())
        return self.html_answer


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    html_generator = HtmlGenerator()
    html_page = html_generator.get_html()
    return [html_page.encode('utf8')]
