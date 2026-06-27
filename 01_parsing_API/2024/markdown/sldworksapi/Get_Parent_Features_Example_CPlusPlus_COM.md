---
title: "Get Parent Features Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Parent_Features_Example_CPlusPlus_COM.htm"
---

# Get Parent Features Example (C++ COM)

This example shows how to get the parent features of the selected feature.

// -------------------------------------------------------------------

STDMETHODIMP CAPITestATL::API_Test(void)

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AFX_MANAGE_STATE(AfxGetStaticModuleState());

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULTkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= S_OK;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<ISldWorks>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSldWorks;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IModelDoc2>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<ISelectionMgr>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSelMgr;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IUnknown>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pUnk;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComQIPtr
<IFeature>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSelFeat;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}NumParents
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}i
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}IFeature**kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pParentsOfFeature
= NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}try

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Connect to SOLIDWORKS application

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(m_iSldWorks);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= m_iSldWorks->get_IActiveDoc2(&pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pModel->get_ISelectionManager(&pSelMgr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pSelMgr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSelMgr->IGetSelectedObject5(1,
&pUnk);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pUnk);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSelFeat
= pUnk;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pSelFeat);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSelFeat->IGetParentCount(&NumParents);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(NumParents
> 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pParentsOfFeature
= new IFeature * [NumParents];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ZeroMemory(pParentsOfFeature,
NumParents * sizeof(IFeature *));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSelFeat->IGetParents(pParentsOfFeature);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
For debugging purposes only

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(i = 0; i < NumParents; i++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComBSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sFeatName;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComBSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sTypeName;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pParentsOfFeature[i]->get_Name(&sFeatName);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pParentsOfFeature[i]->GetTypeName(&sTypeName);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}try

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Clean up each object in the list

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(i = 0; i < NumParents; i++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(pParentsOfFeature[i] != NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pParentsOfFeature[i]->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pParentsOfFeature[i]
= NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}catch
(...)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}DebugBreak();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}catch
(...)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}DebugBreak();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}delete
[] pParentsOfFeature;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return
S_OK;

}

// -------------------------------------------------------------------
