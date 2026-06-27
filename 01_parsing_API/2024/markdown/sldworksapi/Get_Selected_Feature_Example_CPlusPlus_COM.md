---
title: "Get Selected Feature Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Selected_Feature_Example_CPlusPlus_COM.htm"
---

# Get Selected Feature Example (C++ COM)

## Get Selected Feature Example

This example shows how to get the selected
feature and its type, and return the object to the calling method.

LPFEATURE CGetSelectedFeatureApp::GetSelectedFeature1(
LPMODELDOC2 pModelDoc, CString* Message )

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
lres = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPSELECTIONMGR
pSelectMgr = NULL;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULT
hres =NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPUNKNOWN
pUnk = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPFEATURE
pSelectedFeature = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}BSTR
bFeatureTypeName;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}BSTR
bFeatureName;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the Selection Manager for this doc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(S_OK
!= pModelDoc->get_ISelectionManager(
&pSelectMgr ) ||

pSelectMgr == NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message
= "Unable to get the Selection Manager.\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else
if(S_OK != pSelectMgr->GetSelectedObjectType(
1, &lres )

|| lres == 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the Selected Object type

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message
= "No Feature is currently selected.\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else
if(S_OK != pSelectMgr->IGetSelectedObject2(
1, &pUnk )

|| pUnk == NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the Selected Object of Unknown Type

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message
= "Unable to get the selected Object.\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else
if(S_OK != pUnk->QueryInterface( IID_IFeature,

(LPVOID *)&pSelectedFeature) || pSelectedFeature ==
NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the Selected Feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message
= "Unable to get the selected Feature.\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else
if(S_OK != pSelectedFeature->GetTypeName(&bFeatureTypeName)||

bFeatureTypeName == NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the Selected Feature Type Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message
= "Unable to get the selected Feature Type Name.\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else
if(S_OK != pSelectedFeature->get_Name(&bFeatureName)||

bFeatureName == NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the Selected Feature Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message
= "Unable to get the selected Feature Name.\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Everything is okay. Clean up and report back with object.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Release the Selection Manager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSelectMgr->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Release the unknown object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pUnk->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Form the return message

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CString
FeatureTypeName(bFeatureTypeName);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CString
FeatureName(bFeatureName);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message
= "Found a Feature called " + FeatureName + " of type "

+ FeatureTypeName + ".\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SysFreeString(bFeatureTypeName);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SysFreeString(bFeatureName);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Return with Feature object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return
pSelectedFeature;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Something went wrong. Clean up and report back without object.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Release the Selection Manager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(pSelectMgr)pSelectMgr->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Release the unknown object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(pUnk)pUnk->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Return with no object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return
NULL;

}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}
