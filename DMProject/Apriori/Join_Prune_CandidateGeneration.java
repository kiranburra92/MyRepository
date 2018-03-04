import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class Join_Prune_CandidateGeneration {

	static ArrayList<List<Integer>> candidateGeneration(int k) {
		
	/*** Apriori Algorithm Join Step ***/
		
		HashSet<List<Integer>> candidateHashSet= new HashSet<List<Integer>>();
		
		for(int i = 0; i < (GenerateFrequentItemset.frequentItemset.size() - 1); i++){
			
			for(int j = i + 1; j < GenerateFrequentItemset.frequentItemset.size(); j++){
				
				Set<Integer> joinF1F2 = new TreeSet<Integer>();
				
				for(int f = 0; f < GenerateFrequentItemset.frequentItemset.get(i).size(); f++){

					joinF1F2.add(GenerateFrequentItemset.frequentItemset.get(i).get(f));
				}
				 
				for(int f = 0; f < GenerateFrequentItemset.frequentItemset.get(j).size(); f++){

					joinF1F2.add(GenerateFrequentItemset.frequentItemset.get(j).get(f));
				}

				candidateHashSet.add(new ArrayList<Integer>(joinF1F2));		// Ck --> Ck union {c}
			}
		}
		
		ArrayList<List<Integer>> candidateItemset= new ArrayList<List<Integer>>(candidateHashSet);
		
	/*** Apriori Algorithm Prune Step - Based on Downward Closure Property***/
		
		ArrayList<ArrayList<Integer>> subsetResults = new ArrayList<>();
		
		for(int c = 0; c < candidateItemset.size(); c++ ){
			subsetResults = get_KMinus1_Subsets(candidateItemset.get(c),(k-1),0,new ArrayList<Integer>(),new ArrayList<>());	// Generating k-1 subsets 
			
			if(!(GenerateFrequentItemset.frequentItemset.containsAll(subsetResults))){
				candidateItemset.set(c, null);
			}
		}
		candidateItemset.removeAll(Collections.singleton(null));		// This will remove all Null Items from the ArrayList
		
		return candidateItemset;
		
	}

	/*** Generating (k-1) subsets of each candidateItemset ***/
	
		private static ArrayList<ArrayList<Integer>> get_KMinus1_Subsets(List<Integer> candidateItemset, int k, int index, List<Integer> currentSet,ArrayList<ArrayList<Integer>> resultSet) {
		    
		    if (currentSet.size() == k) {
		    	resultSet.add(new ArrayList<Integer>(currentSet));
		        return resultSet;
		    }
		    
		    if (index == candidateItemset.size()) return resultSet;

		    Integer value = candidateItemset.get(index);
		    currentSet.add(value);
		    
		    get_KMinus1_Subsets(candidateItemset, k, index+1, currentSet, resultSet);
		    currentSet.remove(value);

		    get_KMinus1_Subsets(candidateItemset, k, index+1, currentSet, resultSet);
		    
		    return resultSet;
		}

}
