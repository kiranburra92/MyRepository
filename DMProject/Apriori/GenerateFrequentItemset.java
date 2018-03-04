import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GenerateFrequentItemset {
	
	static ArrayList<List<Integer>> frequentItemset= new ArrayList<List<Integer>>();
	
	/*** Create HashMap with Candidate Items for Easy Comparison ***/
	
	static Map<Integer, List<List<Integer>>> createCandidateHashMap(List<List<Integer>> candidateItemset) {
		
		Map<Integer, List<List<Integer>>> candidateItemsetHashMap = new HashMap<Integer, List<List<Integer>>>();
		
		for(int outer =0; outer < candidateItemset.size(); outer++){
			int item = candidateItemset.get(outer).get(0);	
			List<List<Integer>> itemList = new ArrayList<>(); 
			if (candidateItemsetHashMap.get(item) != null) {
				itemList = candidateItemsetHashMap.get(item);
				}
			itemList.add(candidateItemset.get(outer));
			candidateItemsetHashMap.put(item, itemList );
		}
		return candidateItemsetHashMap;
	}
	 
	/*** Support Count of Each Candidate Itemset ***/
	
	public static Map<List<Integer>, Integer> candidateSupportCount(Map<Integer, List<List<Integer>>> candidateItemsetHashMap, int k) {
		
	    Map<List<Integer>, Integer> supportCount = new HashMap<>();
	    
	    for(int outer = 0; outer < FrequentK_MiningDriver.transactionAfterIntegerMap.size(); outer++){
	    	
	    	List<Integer> oneTransactionLine = new ArrayList<Integer>(FrequentK_MiningDriver.transactionAfterIntegerMap.get(outer));
	    	
	    	boolean flag = false;
	    	
	    	List<List<Integer>> candidateItemsetCompareList = new ArrayList<List<Integer>>();
	    		
	    	for(int t = 0; t <= (oneTransactionLine.size() - k) ; t++ ){
	    		int transactionItem = oneTransactionLine.get(t);
	    		if(candidateItemsetHashMap.get(transactionItem) != null){
	    			candidateItemsetCompareList.addAll(candidateItemsetHashMap.get(transactionItem));
	    		}
	    	}
	    	if(candidateItemsetCompareList != null){
		    	for(int c = 0; c < candidateItemsetCompareList.size(); c++){
		    		
		    		List<Integer> itemset = candidateItemsetCompareList.get(c);
			   		
		    		if(oneTransactionLine.containsAll(itemset)){
			   			
			   			supportCount.put(itemset, supportCount.getOrDefault(itemset, 0) + 1);
			   			
			   			flag = true;			// It means that Transaction 't' contains atleast 1 candidate itemset, matched with it
			   			if(oneTransactionLine.size() == k){
		    				break;
		    			}
		   			}
		   		}
	    	}
		    if(flag == false){
		    	FrequentK_MiningDriver.transactionAfterIntegerMap.set(outer, null);
		   	}
	    	
		}
	    FrequentK_MiningDriver.transactionAfterIntegerMap.removeAll(Collections.singleton(null));  

	    return supportCount;
	}

	/*** Frequent Itemset Generation ***/
	
	public static void frequentItemsetGeneration(Map<Integer, List<List<Integer>>> candidateItemsetHashMap, int k) {
		
		Map<List<Integer>, Integer> supportCount = candidateSupportCount(candidateItemsetHashMap, k);
		
		frequentItemset= new ArrayList<List<Integer>>();
		
		ArrayList<Integer> frequentItemsetSupportCount = new ArrayList<Integer>();
		
		for(Map.Entry<List<Integer>, Integer> mapEntry: supportCount.entrySet()){
			if(mapEntry.getValue() >= FrequentK_MiningDriver.minSupport ){
				frequentItemset.add(mapEntry.getKey());
		    	frequentItemsetSupportCount.add(mapEntry.getValue());
		   	}
        }
		
		/***  Printing to Output File - Map Integers back to Unique Reviewer IDs ***/
		
		if(k == FrequentK_MiningDriver.inputKValue){
			try {
				PrintWriter writer = new PrintWriter(FrequentK_MiningDriver.outputFileName, "UTF-8");
				
				for(int outer = 0; outer < frequentItemset.size(); outer++){
					ArrayList<String> frequentReviewIDs = new ArrayList<String>();
					for(int j = 0; j < frequentItemset.get(outer).size(); j++){
						
						int temp = frequentItemset.get(outer).get(j);
						for(Map.Entry<String,Integer> entry: ReviewerID_StringToIntConversion.uniqueReviewerIDs_Integer.entrySet()){
					    	if(temp == entry.getValue()){
					    		frequentReviewIDs.add(entry.getKey());  
					    		break;
					    	}
					    }
					} 			
					
						for(int f = 0; f < frequentReviewIDs.size(); f++){
							writer.print(frequentReviewIDs.get(f) + " ");
						}
						if(frequentItemsetSupportCount.size() != 0){
							writer.println("(" + frequentItemsetSupportCount.get(outer) + ")");
						}	
					
				}
	            writer.close();
	            
			} catch (FileNotFoundException | UnsupportedEncodingException e) {
				e.printStackTrace();
			}
		}		
		
	}
}
