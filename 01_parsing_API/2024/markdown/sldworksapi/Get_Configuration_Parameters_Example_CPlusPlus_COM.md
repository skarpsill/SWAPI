---
title: "Get Configuration Parameters Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Configuration_Parameters_Example_CPlusPlus_COM.htm"
---

# Get Configuration Parameters Example (C++ COM)

This example shows how to get the parameters for the specified configuration.

'--------------------------------

'

' Preconditions: Part is open and has a configuration
named aaa.

'

' Postconditions: None

'

'---------------------------------

#define USING_DEBUG_SOLIDWORKSkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}TRUE

#ifdef _DEBUG && USING_DEBUG_SOLIDWORKS

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}#define
AFX_MANAGE_STATE_ADDINkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AFX_MANAGE_STATE(AfxGetAppModuleState());

#else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}#define
AFX_MANAGE_STATE_ADDINkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AFX_MANAGE_STATE(AfxGetStaticModuleState());

#endif

// -------------------------------------------------------------------

STDMETHODIMP CAPITestATL::API_Test(void)

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AFX_MANAGE_STATE_ADDIN;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULTkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= S_OK;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<ISldWorks>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSldWorks;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IModelDoc2>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IConfigurationManager>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCfgMgr;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComBSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sCfgName(_T("aaa"));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}NumParams
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}i
= 0;

BSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*vNames
= NULL;

BSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*vValues
= NULL;

VARIANT_BOOLkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bret
= VARIANT_FALSE;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}try

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Connect to SOLIDWORKS

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(m_iSldWorks);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= m_iSldWorks->get_IActiveDoc2(&pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pModel->get_ConfigurationManager(&pCfgMgr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pCfgMgr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pCfgMgr->GetConfigurationParamsCount(sCfgName,
&NumParams);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(NumParams
> 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vNameskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}= new BSTR[NumParams];kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(vNames
);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vValues
= new BSTR[NumParams];kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(vValues);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pCfgMgr->IGetConfigurationParams(sCfgName,
NumParams, vNames, vValues, &bret);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(bret);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(i = 0; i < NumParams; i++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComBSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sName
;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComBSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sValue;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sName
.Attach(vNames [i]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sValue.Attach(vValues[i]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}OutputDebugString(sName
);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}OutputDebugString(_T("\n"));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}OutputDebugString(sValue);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}OutputDebugString(_T("\n"));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}delete
[] vNames ;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}delete
[] vValues ;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}catch
(...)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}DebugBreak();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}delete
[] vNames ;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}delete
[] vValues ;

return S_OK;

}
