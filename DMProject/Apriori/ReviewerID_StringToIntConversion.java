import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class ReviewerID_StringToIntConversion {
	
	static HashMap<String,Integer> uniqueReviewerIDs_Integer;
	
	/***  Map Unique Reviewer IDs to Integers ***/
	
	static void mapReviewerIDtoInteger(Set<String> candidateItemsetSize1, List<Set<String>> transactionStringID) {
	
		uniqueReviewerIDs_Integer = new HashMap<String,Integer>();
		
		int id = 0;
		Iterator<String> iterator = candidateItemsetSize1.iterator();
	    while(iterator.hasNext()){
	    	String reviewerID = iterator.next();
	    	uniqueReviewerIDs_Integer.put(reviewerID, id); 
				id++;
	    }
	    
	/***  Transaction DB after Mapping Reviewer IDs to Integers ***/
	    
	    for(int outer = 0; outer < transactionStringID.size(); outer++){
	    	
	    	Set<Integer> reviewerIdInteger = new TreeSet<Integer>(); 
	    	Iterator<String> it = transactionStringID.get(outer).iterator();
	    	
	    	while(it.hasNext()){
	    		String reviewID = it.next();
	    		reviewerIdInteger.add(uniqueReviewerIDs_Integer.get(reviewID));
			}
	    	
	    	FrequentK_MiningDriver.transactionAfterIntegerMap.add(reviewerIdInteger);
		}
	}
}
