import numpy as np 

F = np.array([[1, 1], [0 ,1]])
B = np.array([[0.5, 1]])
H = np.array([[1, 0], [0, 0]])
Q = np.array([[0, 0], [1, 0]])
R = np.array([[4., 0], [0, 1]])
P = np.array([[10 ,0], [0, 0.01]])
g = np.array([[10], [0]])

def kalman(z, prev, P):
    p_state_est = F.dot(prev) +  B.dot(g)
    print(f"predicted_state_est = {p_state_est}")
    p_state_err = F.dot(P.dot(F.T)) + Q
    print(f"Predicted_state_error = {p_state_err}")
    pre_pred_m_err = z - H.dot(p_state_est)
    print(f"pre_predicted_measurement_error  = {pre_pred_m_err}")
    pre_fit_error_cov = H.dot(p_state_err).dot(H.T) + R
    print(f"prefit error covariance = {pre_fit_error_cov}")
    K_gain = p_state_err.dot(H).dot(np.linalg.inv(pre_fit_error_cov))
    print(f"Kalman gain = {K_gain}")
    up_state_estimate = p_state_est + K_gain.dot(pre_pred_m_err)
    print(f"updated state estimate = {up_state_estimate}")
    sub = K_gain.dot(H)
    n = sub.shape[0]
    I = np.identity(n)
    up_state_err = (I - sub).dot(p_state_err)
    print(f"Updated state error = {up_state_err}")
    pfe = z - H.dot(up_state_estimate)
    print(f"Post-fit error = {pfe}")
    return up_state_estimate, up_state_err

state = np.array([[105], [0]])
z = [90, 80, 60, 18]
count = 1
for z_ in z:
    print(f"ITERATION {count}")
    count +=1
    state, P = kalman(z_, state, P)
    