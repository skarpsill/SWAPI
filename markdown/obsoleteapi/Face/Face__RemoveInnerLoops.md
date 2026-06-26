---
title: "Face::RemoveInnerLoops"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__RemoveInnerLoops.htm"
---

# Face::RemoveInnerLoops

This
method is obsolete and has been superseded by[Face2::RemoveInnerLoops](sldworksAPI.chm::/Face2/Face2__RemoveInnerLoops.htm).

Description

This method removes the inner loops on this face.

Syntax (OLE Automation)

retval
= Face.RemoveInnerLoops ( numOfLoops, innerLoopsIn)

(Table)=========================================================

| Input: | (long)
numOfLoops | Number
of loops to be removed |
| --- | --- | --- |
| Input: | (VARIANT)
innerLoopsIn | VARIANT
of type SafeArray of Dispatch pointers to the inner loops to be removed |
| Return: | (LPDISPATCH)
retval | Dispatch
pointer to the resulting face object |

Syntax (COM)

status = Face->IRemoveInnerLoops
( numOfLoops, innerLoopsIn, &retval )

(Table)=========================================================

| Input: | (long) numOfLoops | Number of loops to be removed |
| --- | --- | --- |
| Input: | (LPLOOP*) innerLoopsIn | Pointer to an array of the inner loops to be removed |
| Output: | (LPFACE) retval | Pointer to the resulting face object |
| Return: | (HRESULT)status | S_OK if successful |

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Face_Object$$**$$ZAccessorByCreate$$**$$ZCreateFace$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Face\Face__RemoveInnerLoops.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
