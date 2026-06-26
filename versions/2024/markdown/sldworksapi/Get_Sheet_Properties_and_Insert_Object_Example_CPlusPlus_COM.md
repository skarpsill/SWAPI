---
title: "Get Sheet Properties and Insert Object Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sheet_Properties_and_Insert_Object_Example_CPlusPlus_COM.htm"
---

# Get Sheet Properties and Insert Object Example (C++ COM)

This example shows how to get a sheet's properties and then insert an
object from a file.

STDMETHODIMP CDgtlPen::demo1()

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULTkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= S_OK;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IModelDoc2>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComQIPtr
<IDrawingDoc>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pDraw;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}doublekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSheetProps[7];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<ISheet>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSheet;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}BOOLkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}createLink
= FALSE;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}doublekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}x
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}doublekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}y
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}doublekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}z
= 0;

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

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ZeroMemory(pSheetProps,
7 * sizeof(double));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSheet->IGetProperties(pSheetProps);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}y
= pSheetProps[6];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pModel->InsertObjectFromFile(CComBSTR(_T("C:/Bitmaps/digitalpen.bmp")), createLink, x, y,
z, &retval);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return
S_OK;

}
