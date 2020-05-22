# fast-pub

A market and trade gateway using [ctpbee](https://github.com/ctpbee/ctpbee) 

## Description 
try to use fastapi and ctpbee to build a reliable gateway 

## Destination
support 200 account 

## start server command

```
uvicorn fast:fast_api --reload
```

## interface document 
> using fastapi to generate
>

## bugs
1. when insert two apps, the signals do not spilt as I want. 
2. should we share the timer event between apps ? 