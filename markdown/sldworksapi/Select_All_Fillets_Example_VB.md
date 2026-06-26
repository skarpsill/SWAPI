---
title: "Select All Fillets Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_All_Fillets_Example_VB.htm"
---

# Select All Fillets Example (VBA)

Selecting all of the fillets on an active part is done by iterating
through all of the features with IModelDoc2::FirstFeature and IFeature::GetNextFeature.
For each feature, check the type with IFeature::GetTypeName and compare
it to the "Fillet" and "VarFillet" constants to see
if the current feature is a fillet.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
the feature is a fillet, then place the fillet in an IEntity object and
select the entity.

'------------------------------------------------------------------

'

' Preconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)
Part document is open.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)
Fillets exist on the part.

'

' Postconditions: All of the fillets are selected.

'

'------------------------------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim Model As SldWorks.ModelDoc2

Dim CurFeature As SldWorks.feature

Dim CurEntity As SldWorks.entity

Dim SelData As SldWorks.SelectData

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the SOLIDWORKS object and the active model

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = GetObject(, "SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Model = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the first feature on the part

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
CurFeature = Model.FirstFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
For all of the features on the part

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Do
While Not CurFeature Is Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
If the current feature is one of the fillet types,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
then select the current fillet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
CurFeature.GetTypeName= "Fillet"
Or CurFeature.GetTypeName= "VarFillet"
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
CurEntity = CurFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CurEntity.Select4True, SelData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Go
to the next feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
CurFeature = CurFeature.GetNextFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Loop

End Sub
