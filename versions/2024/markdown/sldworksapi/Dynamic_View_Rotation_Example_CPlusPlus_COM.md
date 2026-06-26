---
title: "Dynamic View Rotation Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Dynamic_View_Rotation_Example_CPlusPlus_COM.htm"
---

# Dynamic View Rotation Example (C++ COM)

## Dynamically Rotate Model View Example (C++ COM)

This example shows how to dynamically rotate
a model view. It also shows you how to speed up the process by using the
StartDynamics and StopDynamics calls.

RotateTheView(ISldWorks* m_pSldWorks)

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPMODELDOC2
p_ModelDoc = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPMODELVIEW
p_ModelView = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULT
res = S_OK;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Retrieve the model document pointer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}res
= m_pSldWorks->get_IActiveDoc2(
&p_ModelDoc );kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(
res != S_OK || p_ModelDoc == NULL )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the active view pointer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}res
= p_ModelDoc->get_IActiveView(&p_ModelView);kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(
res != S_OK || p_ModelView == NULL )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}p_ModelDoc->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
i;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Prepare view for rotation

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}p_ModelView->StartDynamics();kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(i = 1; i < 100; i++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}p_ModelDoc->ViewRotateplusy();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
End dynamic rotation mode

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}p_ModelView->StopDynamics();kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Repaint the screen

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}p_ModelDoc->GraphicsRedraw2();kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Clean
up

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}p_ModelView->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}p_ModelDoc->Release();

}
