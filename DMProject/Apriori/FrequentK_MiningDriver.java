import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class FrequentK_MiningDriver {
	
	static int minSupport; 
	static int inputKValue;
	static String outputFileName;
	
	static List<Set<Integer>> transactionAfterIntegerMap = new ArrayList<Set<Integer>>();
		
	public static void main(String[] args) throws IOException
    {
		if(args.length != 4)
        {
            System.out.println("Please provide the Input Values in following order :");
            System.out.println("<min_sup> <k> <input_transaction_file_path> <output_file_path>");
            System.exit(0);
        }
		Long startTime = System.currentTimeMillis();
		
		minSupport = Integer.parseInt(args[0]);
        inputKValue = Integer.parseInt(args[1]);
        outputFileName = args[3];
        
        String inputTransactionFileName = args[2];
        
        FileReader fileReader = new FileReader(inputTransactionFileName);
		BufferedReader bufferedReader = new BufferedReader(fileReader);
		List<Set<String>>transaction = new ArrayList<Set<String>>();
		
		Set<String> candidateItemsetSize1 = new TreeSet<String>(); 
		
		String line;
		while((line = bufferedReader.readLine()) != null) {
			String[] eachReviewerID = line.split(" ");
			
			if(eachReviewerID.length >= inputKValue){
				Set<String> reviewerId = new TreeSet<String>();
				for(int i = 0; i < eachReviewerID.length; i++){
					candidateItemsetSize1.add(eachReviewerID[i]);
					reviewerId.add(eachReviewerID[i]);
				}
				transaction.add(reviewerId);
			}
			
		}
		fileReader.close();
		
		ReviewerID_StringToIntConversion.mapReviewerIDtoInteger(candidateItemsetSize1,transaction);
		List<Integer> frequentItemsetSize1 =  GenerateFrequentItemsetSize1.GenerateFrequent_1_Itemset(candidateItemsetSize1);
    
	    ExecutorService executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        executorService.execute(new Runnable() {
            @Override
            public void run() {
        	    for(int k = 2; k <= inputKValue ; k++){			

        	    	if(k==2){
        	    		
        	    		/*** For Optimization & Performance Upgrade ***/
        	    		
        	    		Map<Integer, List<List<Integer>>> candidateItemsetHashMap = new HashMap<Integer, List<List<Integer>>>();
        	    		
        	    		for(int i = 0; i < (frequentItemsetSize1.size() - 1); i++){
        	    			for(int j = i + 1; j < frequentItemsetSize1.size(); j++){
        	    				 
        	    				List<List<Integer>> itemList = new ArrayList<>(); 
        	    				
        	    				if (candidateItemsetHashMap.get(frequentItemsetSize1.get(i)) != null) {
        	    					itemList = candidateItemsetHashMap.get(frequentItemsetSize1.get(i));
        	    					}
        	    				itemList.add(Arrays.asList(frequentItemsetSize1.get(i), frequentItemsetSize1.get(j)));
        	    				candidateItemsetHashMap.put(frequentItemsetSize1.get(i), itemList );
         	    			}
        	    		}
         	    		GenerateFrequentItemset.frequentItemsetGeneration(candidateItemsetHashMap, k);
        	    	}
        	    	else{
        	    		ArrayList<List<Integer>> candidateItemset = Join_Prune_CandidateGeneration.candidateGeneration(k);
        	    		
        	    		Map<Integer, List<List<Integer>>> candidateItemsetHashMap = GenerateFrequentItemset.createCandidateHashMap(candidateItemset);

        	    		GenerateFrequentItemset.frequentItemsetGeneration(candidateItemsetHashMap, k);
        	    	}
        	    }
            }
        });
        
        executorService.shutdown();
        while (!executorService.isTerminated()){

        }
    Long endTime = System.currentTimeMillis();

    System.out.println("\n Time taken in seconds: "+(endTime - startTime)/1000);
    }
}
