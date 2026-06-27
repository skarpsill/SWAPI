---
title: "Insert Spline in Drawing Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Spline_in_Drawing_Example_CPlusPlus_COM.htm"
---

# Insert Spline in Drawing Example (C++ COM)

This example shows how to insert a spline in a drawing.

STDMETHODIMP CDgtlPen::demo3()

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULTkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= S_OK;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IModelDoc2>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComQIPtr
<IDrawingDoc>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pDraw;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IView>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pView;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IView>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pFocusLockedView;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<ISheet>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSheet;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}intkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pPropArray[4];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}doublekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pKnotsArray[11];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}doublekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[21];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VARIANT_BOOLkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}updateEditRebuild
= TRUE;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}retval
= NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VARIANT_BOOLkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}focusLocked
= NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ZeroMemory(pPropArray,
4 * sizeof(int));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ZeroMemory(pKnotsArray,
11 * sizeof(double));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ZeroMemory(pCntrlPntCoordArray,
21 * sizeof(double));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pPropArray[0]
= 3;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Dimension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pPropArray[1]
= 4;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Order

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pPropArray[2]
= 7;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Number
of control Points

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pPropArray[3]
= 0;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Periodicity

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pKnotsArray[0]
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pKnotsArray[1]
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pKnotsArray[2]
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pKnotsArray[3]
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pKnotsArray[4]
= 0.3;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pKnotsArray[5]
= 0.3;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pKnotsArray[6]
= 0.6;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pKnotsArray[7]
= 1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pKnotsArray[8]
= 1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pKnotsArray[9]
= 1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pKnotsArray[10]
= 1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[0]
= -0.1;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[1]
= -0.009;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[2]
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[3]
= -0.11;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[4]
= 0.013;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[5]
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[6]
= -0.14;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[7]
= 0.035;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[8]
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[9]
= 0.015;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[10]
= 0.019;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[11]
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[12]
= -0.059;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[13]
= -0.024;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[14]
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[15]
= 0.012;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[16]
= -0.018;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[17]
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[18]
= 0.054;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[19]
= -0.013;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCntrlPntCoordArray[20]
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= m_iSldWorks->get_IActiveDoc2(&pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_ASSERT(pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pDraw
= pModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_ASSERT(pDraw);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pDraw->IGetFirstView(&pView);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_ASSERT(pView);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}while(pView
!= NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IView>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pNextView;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pView->get_FocusLocked(&focusLocked);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(focusLocked)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pFocusLockedView
= pView;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_ASSERT(pView);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pView
= NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pView->IGetNextView(&pNextView);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pView
= NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pView
= pNextView;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pDraw->IGetCurrentSheet(&pSheet);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_ASSERT(pSheet);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSheet->get_FocusLocked(&focusLocked);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSheet->put_FocusLocked(TRUE);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pModel->InsertSketch2(updateEditRebuild);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pModel->ISketchSplineByEqnParams(pPropArray,
pKnotsArray, pCntrlPntCoordArray, &retval);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_ASSERT(retval);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSheet->put_FocusLocked(focusLocked);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(pFocusLockedView
!= NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pFocusLockedView->put_FocusLocked(TRUE);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pModel->GraphicsRedraw2();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return
S_OK;

}
