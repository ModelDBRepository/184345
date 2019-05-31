'''
Defines a class, Neuron473872986, of neurons from Allen Brain Institute's model 473872986

A demo is available by running:

    python -i mosinit.py
'''
class Neuron473872986:
    def __init__(self, name="Neuron473872986", x=0, y=0, z=0):
        '''Instantiate Neuron473872986.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron473872986_instance is used instead
        '''
        
        # load the morphology
        from load_swc import load_swc
        load_swc('Scnn1a-Tg3-Cre_Ai14_IVSCC_-180214.05.01.01_475124505_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
        
        self._name = name
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron473872986_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im_v2', u'K_T', u'Kd', u'Kv2like', u'Kv3_1', u'NaV', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 121.95
            sec.e_pas = -96.2065906525
        for sec in self.apic:
            sec.cm = 2.73
            sec.g_pas = 1.16532586232e-06
        for sec in self.axon:
            sec.cm = 1.0
            sec.g_pas = 0.000294993818716
        for sec in self.dend:
            sec.cm = 2.73
            sec.g_pas = 4.40627823892e-07
        for sec in self.soma:
            sec.cm = 1.0
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Ih = 0
            sec.gbar_NaV = 0.0982495
            sec.gbar_Kd = 0.000159105
            sec.gbar_Kv2like = 0.12126
            sec.gbar_Kv3_1 = 0.395921
            sec.gbar_K_T = 0.0201728
            sec.gbar_Im_v2 = 0.00634387
            sec.gbar_SK = 0.000183294
            sec.gbar_Ca_HVA = 0.000306911
            sec.gbar_Ca_LVA = 3.4459e-05
            sec.gamma_CaDynamics = 0.0229384
            sec.decay_CaDynamics = 526.092
            sec.g_pas = 0.000100664
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

