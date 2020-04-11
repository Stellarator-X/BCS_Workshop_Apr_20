// Rosenfields algorithm
INPUT: M , a binary matrix with value 0 at background pixels and 1 for non-background pixels
OUTPUT: L, the labelled image matrix
function rosen
    // First Pass
    label_count <- 0
    for i in range(number of rows of M)
        for j in range(number of columns of M)
            if both label(M[i, j-1]) and label(M[i-1, j]) are NULL
                label_count <- label_count + 1
                set label_count as a root
                set label(M[i, j]) as label_count
            else
                set label(M[i,j]) as min(label(M[i, j-1]), label(M[i-1, j]))
                if label(M[i, j-1]) not equal to label(M[i-1, j])
                    set max(label(M[i, j-1]), label(M[i-1, j])) as child of min(label(M[i, j-1]), label(M[i-1, j]))
                end if
            end if
        end for
    end for
    // Second pass
    for i in range(number of rows of M)
        for j in range(number of columns of M)
            for l in range(1 to label_count)
                if label(M[i,j])  is a child of l
                    set label(M[i, j]) as l
        end for
    end for
end function

ITERATION 1
predicted_state_est = [[110.]
 [  5.]]
Predicted_state_error = [[1.001e+01 1.000e-02]
 [1.000e-02 1.000e-02]]
pre_predicted_measurement_error  = [[-20.]
 [ 90.]]
prefit error covariance = [[14.01  0.  ]
 [ 0.    1.  ]]
Kalman gain = [[7.14489650e-01 0.00000000e+00]
 [7.13775874e-04 0.00000000e+00]]
updated state estimate = [[95.710207  ]
 [ 4.98572448]]
Updated state error = [[2.85795860e+00 2.85510350e-03]
 [2.85510350e-03 9.99286224e-03]]
Post-fit error = [[-5.710207]
 [90.      ]]
ITERATION 2
predicted_state_est = [[105.69593148]
 [  9.98572448]]
Predicted_state_error = [[2.87366167 0.01284797]
 [0.01284797 0.00999286]]
pre_predicted_measurement_error  = [[-25.69593148]
 [ 80.        ]]
prefit error covariance = [[6.87366167 0.        ]
 [0.         1.        ]]
Kalman gain = [[0.41806854 0.        ]
 [0.00186916 0.        ]]
updated state estimate = [[94.95327103]
 [ 9.9376947 ]]
Updated state error = [[1.67227414 0.00747664]
 [0.00747664 0.00996885]]
Post-fit error = [[-14.95327103]
 [ 80.        ]]
ITERATION 3
predicted_state_est = [[109.89096573]
 [ 14.9376947 ]]
Predicted_state_error = [[1.69719626 0.01744548]
 [0.01744548 0.00996885]]
pre_predicted_measurement_error  = [[-49.89096573]
 [ 60.        ]]
prefit error covariance = [[5.69719626 0.        ]
 [0.         1.        ]]
Kalman gain = [[0.29790026 0.        ]
 [0.00306212 0.        ]]
updated state estimate = [[95.02843395]
 [14.78492272]]
Updated state error = [[1.19160105 0.01224847]
 [0.01224847 0.00991543]]
Post-fit error = [[-35.02843395]
 [ 60.        ]]
ITERATION 4
predicted_state_est = [[114.81335666]
 [ 19.78492272]]
Predicted_state_error = [[1.22601341 0.0221639 ]
 [0.0221639  0.00991543]]
pre_predicted_measurement_error  = [[-96.81335666]
 [ 18.        ]]
prefit error covariance = [[5.22601341 0.        ]
 [0.         1.        ]]
Kalman gain = [[0.23459821 0.        ]
 [0.00424107 0.        ]]
updated state estimate = [[92.10111607]
 [19.37433036]]
Updated state error = [[0.93839286 0.01696429]
 [0.01696429 0.00982143]]
Post-fit error = [[-74.10111607]
 [ 18.        ]]