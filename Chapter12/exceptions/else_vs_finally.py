try:
    print(10 / 2)

except Exception as e:
    print(e)

else:
    # Runs only if there is no exception
    print("No exception")

finally:
    # Runs no matter what
    print("Finally")
