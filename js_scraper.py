import os       # Import os module for file system operations
import time     # Import time module for sleep functionality
import requests # Import requests module for HTTP requests


# Base path for saving the data files
data_base_path = './data/'

# Headers to mimic a request from a browser to avoid potential blocking by the server
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/95.0.4638.69 Safari/537.36'
}

# Loop through a range of offsets, incrementing by 15 each time
for i in range(356865, 500000, 15):
    try:
        # Construct the URL with the current offset
        url = '' \
              '.js?last_date=2021-11-12&limit=15&offset={}'.format(i)
        
        # Send an HTTP GET request to the URL with the specified headers
        r = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if r.status_code == 200:
            # Save the response text to a file named after the current offset
            with open(os.path.join(data_base_path, '{}.js'.format(i)), 'w') as f:
                f.writelines(r.text)
        else:
            # Print a message if the response status code is not 200
            print('Got non-200 response at {}'.format(i))

        # Print a completion message and pause for 5 seconds before the next iteration
        print('Done {}. Pausing before continuing...'.format(i))
        time.sleep(5)
    except requests.exceptions.RequestException:
        # Handle any request-related exceptions
        print('Request exception at {}'.format(i))
    except Exception as e:
        # Handle any other exceptions
        print('Exception: {}'.format(e))