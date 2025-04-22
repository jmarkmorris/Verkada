- perhaps we could add a fictitious user for each LPOI.
- that user can have an associated email address
- then when we seen an event for an LPOI we can send that to the user email

- more api's to test
- still need to figure out how to get events.
- one option is to poll helix every so many minutes.
- have to watch for getting rate limited
- have to handle overlaps and seeing event multiples and quashing those.


1. wake up
2. poll for events this period
3. get all lpoi
4. look up user by lpoi?
5. create/send email
6. when done with all new events, go to sleep