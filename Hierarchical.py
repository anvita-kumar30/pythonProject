# import numpy as np
class Distance_computation_grid(object):
    def __init__(self):
        pass
    def compute_distance(self, samples):
        Distance_mat = np.zeros((len(samples), len(samples)))
        for i in range(Distance_mat.shape[0]):
            for j in range(Distance_mat.shape[0]):
                if i!=j:
                    Distance_mat[i,j] = float(self.distance_calculate(samples[i],samples[j]))
                else:
                    Distance_mat[i,j] = 10**4
        return Distance_mat
    #For two samples
    def distance_calculate(self, sample1, sample2):
        dist = []
        for i in range(len(sample1)):
            for j in range(len(sample2)):
                try:
                    dist.append(np.linalg.norm(np.array(sample1[i])-np.array(sample2[j])))
                except:
                    dist.append(self.intersampledist(sample1[i], sample2[j]))
        return min(dist)
    #For one sample and one cluster
    def intersampledist(self, s1, s2):
        # if str(type(s2[0]))!='<class \'list\'>':
        #     s2=[s2]
        # if str(type(s1[0]))!='<class \'list\'>':
        #     s1=[s1]
        if not isinstance(s2[0], list):
            s2 = [s2]
        if not isinstance(s1[0], list):
            s1 = [s1]
        m = len(s1)
        n = len(s2)
        dist = []
        if n>=m:
            for i in range(n):
                for j in range(m):
                    if (len(s2[i])>=len(s1[j])) and isinstance(s2[i][0], type('str')):
                        dist.append(self.interclusterdist(s2[i], s1[j]))
                    else:
                        dist.append(np.linalg.norm(np.array(s2[i])-np.array(s1[j])))
        else:
            for i in range(m):
                for j in range(n):
                    if (len(s1[i])>=len(s2[j])) and isinstance(s1[i][0], type('str')):
                        dist.append(self.interclusterdist(s1[i],s2[j]))
                    else:
                        dist.append(np.linalg.norm(np.array(s1[i])-np.array(s2[j])))
        return min(dist)
    #For two clusters
    def interclusterdist(self, cl, sample):
        # if sample[0]!='<class \'list\'>':
        #     sample = [sample]
        if not isinstance(sample[0], list):
            sample = [sample]
        dist = []
        for i in range(len(cl)):
            for j in range(len(sample)):
                dist.append(np.linalg.norm(np.array(cl[i])-np.array(sample[j])))
        return min(dist)

# X = np.random.rand(10, 2)  # Example data for X

progression = [[i] for i in range(X.shape[0])]
samples = [[list(X[i])] for i in range(X.shape[0])]
m = len(samples)
distcal = Distance_computation_grid()

while m>1:
    print('Sample size before clustering :- ',m)
    Distance_mat = distcal.compute_distance(samples)
    # sample_ind_needed = np.where(Distance_mat==Distance_mat.min())[0]
    sample_ind_needed = np.unravel_index(np.argmin(distance_mat), distance_mat.shape)
    value_to_add = samples.pop(sample_ind_needed[1])
    samples[sample_ind_needed[0]].append(value_to_add)
    print('Cluster Node 1 :-', progression[sample_ind_needed[0]])
    print('Cluster Node 2 :-', progression[sample_ind_needed[1]])
    progression[sample_ind_needed[0]].append(progression[sample_ind_needed[1]])
    progression[sample_ind_needed[0]] = [progression[sample_ind_needed[0]]]
    v = progression.pop(sample_ind_needed[1])
    m = len(samples)
    print('Progression(Current Sample) :-',progression)
    # print('Cluster attained :-',progression[sample_ind_needed[0]])
    print('Cluster attained:', progression[0])
    print('Sample size after clustering :-',m)
    print('\n')
