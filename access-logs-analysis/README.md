## ACCESS LOGS ANALYSIS

Taking a log file called access.log, with the content

```
2023-04-11 10:15:43 user1 LOGIN
2023-04-11 10:17:02 user2 LOGIN
2023-04-11 10:25:31 user1 LOGOUT
2023-04-11 10:27:18 user3 LOGIN
2023-04-11 10:45:00 user1 LOGIN
2023-04-11 11:02:01 user1 LOGOUT
2023-04-11 11:15:09 user3 LOGOUT
```

## Requirements
1. Implement a function that receives the file url and return a dictionary with the total time (minutes) the users were connected.
2. Ignore bad closed sessions (LOGIN without LOGOUT).
3. Optional: Could manage multiple sessions by user.

## Output example
```
{
    "user1": 46,
    "user3": 48,
    "user2": 0
}
```