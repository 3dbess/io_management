import matplotlib.pyplot as plt

def clook_algorithm(initial_position, requests):
    total_head_movement = 0
    order_served = []

    # Sort the requests in ascending order
    sorted_requests = sorted(requests)

    # Find the index where initial_position is in the sorted_requests
    initial_position_index = sorted_requests.index(initial_position)

    # Head movement towards higher track numbers
    for i in range(initial_position_index, len(sorted_requests)):
        order_served.append(sorted_requests[i])
        total_head_movement += abs(sorted_requests[i] - initial_position)
        initial_position = sorted_requests[i]

    # If not already at the beginning and track 0 is in the requests, jump to the beginning
    if 0 in requests and initial_position != 0:
        order_served.append(0)
        total_head_movement += abs(0 - initial_position)  # Move to the beginning
        initial_position = 0

    # Head movement towards higher track numbers (return journey)
    for i in range(initial_position_index):
        order_served.append(sorted_requests[i])
        total_head_movement += abs(sorted_requests[i] - initial_position)
        initial_position = sorted_requests[i]

    return total_head_movement, order_served

def plot_graph(order_served):
    plt.plot(range(len(order_served)), order_served, marker='o')
    plt.title('CLOOK (Circular LOOK) Disk Scheduling Algorithm')
    plt.xlabel('Order Served')
    plt.ylabel('Track Number')
    plt.show()

if __name__ == "__main__":
    # Input initial position and track requests
    initial_position = int(input("Enter initial position of disk arm: "))
    requests_str = input("Enter track requests separated by spaces: ")
    requests = list(map(int, requests_str.split()))

    # Run CLOOK algorithm
    total_head_movement, order_served = clook_algorithm(initial_position, requests)

    # Display results
    print(f"Total Head Movement: {total_head_movement}")
    print(f"Order Served: {order_served}")

    # Plot the graph
    plot_graph(order_served)
