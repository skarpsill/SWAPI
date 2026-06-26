---
title: "Access Selections Example (VBA) - Code"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Access_Selections_Example_VB_Code.htm"
---

# Access Selections Example (VBA) - Code

This example doubles the length of the base extrude.

Dim swApp As SldWorks.SldWorks

Dim Model As ModelDoc2

Dim Component As Component2

Dim CurFeature As Feature

Dim isGood As Boolean

' Will become an ExtrudeFeatureData Object

Dim FeatData As Object

Dim Depth As Double

Dim SelMgr As SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("sldWorks.application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Model = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Make sure that the active document is a part

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Model.GetType <> swDocPART And Model.GetType <> swDocASSEMBLY Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Msg
= "Only allowed on parts or assemblies" ' Define message

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Style
= vbOKOnly ' OK button only

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Title
= "Error" ' Define title

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Call
MsgBox(Msg, Style, Title) ' Display error message

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Exit
Sub ' Exit this program

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
SelMgr = Model.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the selected object (first in the group if there are more than one)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
At this point CurFeature is just a Feature object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
CurFeature = SelMgr.GetSelectedObject6(1,
0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
CurFeature Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Tell the user that nothing is selected

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.SendMsgToUser2"Please select the Base-Extrude.", swMbWarning, swMbOk

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Exit
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the component of the selected feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Needed for AccessSelections()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Component = SelMgr.GetSelectedObjectsComponent3(1,
0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Check the feature's type name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Make sure it is an extrusion

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not CurFeature.GetTypeName= "Extrusion"
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.SendMsgToUser2"Please select the Base-Extrude.", swMbWarning, swMbOk

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Exit
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the extrusion's FeatureData object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
FeatData = CurFeature.GetDefinition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the access selections for the FeatureData object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
The component is NULL when accessing the selections of a standalone part

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
If you are calling AccessSelections from within an assembly, then model

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
would refer to the top-level document in the assembly and component

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
would refer to the actual part

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}isGood
= FeatData.AccessSelections(Model,
Component)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Inform the user of an error

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not isGood Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.SendMsgToUser2"Unable to obtain access selections.", swMbWarning, swMbOk

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Exit
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Change the depth of this extrusion to double its previous depth

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Depth
= FeatData.GetDepth(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}FeatData.SetDepthTrue, Depth * 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Implement the changes to the feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}isGood
= CurFeature.ModifyDefinition(FeatData,
Model, Component)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
If the modify definition failed

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not isGood Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.SendMsgToUser2"Unable to modify feature.", swMbWarning, swMbOk

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Release the selections

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}FeatData.ReleaseSelectionAccess

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub
