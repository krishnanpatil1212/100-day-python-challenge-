try:
    x = int(input("Enter number: "))
    print("Square:", x * x)

except ValueError:
    print("❌ Invalid input")

else:
    print("✅ No error occurred")

finally:
    print("📌 Execution finished")
