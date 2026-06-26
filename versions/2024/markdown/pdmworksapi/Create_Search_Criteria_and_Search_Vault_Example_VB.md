---
title: "Create Search Criteria and Search Vault Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "pdmworksapi/Create_Search_Criteria_and_Search_Vault_Example_VB.htm"
---

# Create Search Criteria and Search Vault Example (VBA)

This example shows how to create a search criteria and search the SOLIDWORKS Workgroup PDM vault using that criteria.

Private Sub Command1_Click()

Dim Options As PDMWorks.PDMWSearchOptions

Dim Criteria As PDMWorks.PDMWSearchCriteria

Dim Results As PDMWorks.PDMWSearchResults

Dim Result As PDMWorks.PDMWSearchResult

Dim i As Integer

Dim cnt As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}On
Error Resume Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Options = Connection.GetSearchOptionsObject

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not Options Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Options.IgnoreCase= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Options.IgnoreLinks= False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Options.IncludeHiddenDocuments= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Options.SearchConfigSpecificProperties= False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Options.SearchOnlyChildrenOf= ""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Options.SearchCriteria.AddCriteriapdmwOr, pdmwDocumentName,
, Contains, "sldprt"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Options.SearchCriteria.AddCriteriapdmwAnd, PDMWConfiguration,
"", Contains, "default"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Options.SearchCriteria.SaveToFile"c:\temp\cri_test.sqy"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Options.SearchCriteria.LoadFromFile"c:\temp\cri_test.sqy"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Results = Connection.Search(Options)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not Results Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cnt
= Results.Count

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To cnt - 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Result = Results(i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AddItemToGrid
Result

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub
