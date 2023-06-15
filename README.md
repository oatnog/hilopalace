# A Responsive Hilo Palace Theater Website

Original: https://hilopalace.com/hpt_event_categories/movies/

Mobile-friendly: https://hilopalace.fly.dev/

## The Problem
My local artsy movie theater has a website ful of useful information. 
However, the Wordpress theme it's using doesn't look good on mobile browsers.

I often find myself out on Hilo Town, wanting to check what's at the Palace that night. And so I go to their website, and pinch and zoom and try to read the little text, and wonder if there's not a better way.

## My Solution
Ideally, the Palace website just needs a bit of an update, fluff the pillows, etc. But in the meantime...

Why not scrape the useful bits and reformat them?

I'd just need a few pieces...

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) is a famously friendly web scraper.
- [TailwindCSS](https://tailwindcss.com/) could make a responsive site easy! or plain CSS3.
- If I'm using BeautifulSoup, I could stay in the Python ecosystem. Flask would be easy, but it had been a while since I'd used [Django](https://www.djangoproject.com/), so why not use that.
- [Fly.io](https://fly.io/) would let me run a little app server, since I'm not going the client-side JS route.

## Stage One

- [x] Scrape and present the current movies page from the Palace theater's site. Just make it readable on a phone.

## Next Steps

- [ ] Add back in links and other formatting
- [ ] Use the Wordpress API to extract info more directly https://hilopalace.com/wp-json/wp/v2/
- [ ] Cache data in a local db rather than fetching it each time (leveraging Django's strengths)
- [ ] Re-do the rest of the site, including non-movie events

## But what about...

As a fun comparision, I might try this project in [Svelte](https://svelte.dev/), or in [Elixir/Phoenix](https://www.phoenixframework.org/). We'll see!
