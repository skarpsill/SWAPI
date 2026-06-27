---
title: "Display of Item in FeatureManager Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_of_Item_in_Feature_Manager_Example_CPlusPlus_COM.htm"
---

# Display of Item in FeatureManager Example (C++ COM)

## Display of Item in FeatureManager Design Tree Example (C++ COM)

This example shows how to change the visibility
of features in the FeatureManager design tree. Import
swconst.tlb.

ToggleFeatureManagerItemDisplay()

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VARIANT_BOOL
flag;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULT
hres;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPMODELDOC2
pModelDoc = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= m_pSldWorks->get_IActiveDoc2(&pModelDoc);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(S_OK == hres && pModelDoc != NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the Selection Manager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPSELECTIONMGR
SelectionMgr = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= pModelDoc->get_ISelectionManager(&SelectionMgr);kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(S_OK != hres || SelectionMgr == NULL )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
numSelObjects;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= SelectionMgr->GetSelectedObjectCount( &numSelObjects );

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(S_OK != hres || S_OK== hres && numSelObjects == 0 )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPUNKNOWN
pSelObject;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
index;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
SelType;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(index=1; index <= numSelObjects; index++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(S_OK
== SelectionMgr->GetSelectedObjectType2(index,&SelType))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(
SelType == swSelBODYFEATURES ||

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelType
== swSelDATUMAXESkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}||

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelType
== swSelDATUMPLANESkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}||

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelType
== swSelDATUMPOINTSkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}||

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelType
== swSelMATESkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}||

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelType
== swSelREFCURVESkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}||

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelType
== swSelREFERENCECURVES ||

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelType
== swSelREFSURFACESkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}||

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelType
== swSelSKETCHES )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(S_OK
== SelectionMgr->IGetSelectedObject3(
index,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}&pSelObject
) && pSelObject != NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPFEATURE
pFeature;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(S_OK
== pSelObject->QueryInterface(IID_IFeature,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(void**)&pFeature))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Determine if the feature is hidden in the

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
FeatureManager design tree

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(S_OK
== pFeature->GetUIState(

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swIsHiddenInFeatureMgr,
&flag))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
If feature is hidden in the

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
FeatureManager design tree, display it,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
otherwise, hide it.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(flag)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

pFeature->SetUIState(

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swIsHiddenInFeatureMgr,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}FALSE);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}else{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pFeature->SetUIState(

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swIsHiddenInFeatureMgr,
TRUE);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Update the Feature Manager Window by performing a Rebuild on the Doc Type

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
doctype;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= pModelDoc->GetType(&doctype);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(doctype == swDocPART )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPPARTDOC
pPartDoc = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Retrieve IPartDoc pointer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= pModelDoc->QueryInterface(IID_IPartDoc, (LPVOID *)&pPartDoc);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(
hres == S_OK );

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= pPartDoc->EditRebuild();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
clean up

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pPartDoc->Release();
// Release the IPartDoc pointer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else
if (doctype == swDocASSEMBLY)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPASSEMBLYDOC
pAssemblyDoc = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Retrieve IAssemblyDoc pointer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= pModelDoc->QueryInterface(IID_IAssemblyDoc,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(LPVOID
*)&pAssemblyDoc);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(
hres == S_OK );

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= pAssemblyDoc->EditRebuild();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
clean up

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pAssemblyDoc->Release();
// Release the IAssemblyDoc pointer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else
if (doctype == swDocDRAWING)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPDRAWINGDOC
pDrawingDoc = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Retrieve IDrawingDoc pointer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= pModelDoc->QueryInterface(IID_IDrawingDoc,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(LPVOID
*)&pDrawingDoc);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(
hres == S_OK );

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= pDrawingDoc->EditRebuild();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
clean up

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pDrawingDoc->Release();
// Release the IDrawingDoc pointer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModelDoc->Release();
// Release the IModelDoc pointer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}
