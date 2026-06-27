---
title: "Set View Display Mode Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_View_Display_Mode_Example_CPlusPlus_COM.htm"
---

# Set View Display Mode Example (C++ COM)

This example shows how to set the display mode of drawing views.

STDMETHODIMP CDgtlPen::demo2()

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULTkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= S_OK;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IModelDoc2>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComQIPtr
<IDrawingDoc>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pDraw;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<ISheet>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSheet;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IView>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSheetView;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IView>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pView;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDisplayMode
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VARIANT_BOOLkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UseParent
= FALSE;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VARIANT_BOOLkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Facetted
= TRUE;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VARIANT_BOOLkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Edges
= TRUE;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VARIANT_BOOLkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}retval
= NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= m_iSldWorks->get_IActiveDoc2(&pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_ASSERT(pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pDraw
= pModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_ASSERT(pDraw);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pDraw->IGetCurrentSheet(&pSheet);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_ASSERT(pSheet);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pDraw->IGetFirstView(&pSheetView);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_ASSERT(pSheetView);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSheetView->IGetNextView(&pView);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_ASSERT(pView);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}while(pView
!= NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IView>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pNextView;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pView->GetDisplayMode2(&swDisplayMode);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}switch(swDisplayMode)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
swWIREFRAME:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
swHIDDEN_GREYED:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
swHIDDEN:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
swSHADED:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
swFACETED_WIREFRAME:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
swFACETED_HIDDEN_GREYED:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
swFACETED_HIDDEN:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pView->SetDisplayMode3(UseParent,
swHIDDEN, Facetted, Edges, &retval);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_ASSERT(retval);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}default
:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_ASSERT(FALSE);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pView->IGetNextView(&pNextView);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Release view

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pView
= NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pView
= pNextView;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return
S_OK;

}
