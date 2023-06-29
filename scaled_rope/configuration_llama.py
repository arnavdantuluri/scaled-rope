from transformers.models.llama.configuration_llama import LlamaConfig as LlamaConfigOriginal

class LlamaConfig(LlamaConfigOriginal):
    def __init__(self, use_xpos=False, position_interpolation_scale=1, transformer_engine=None, **kwargs):
        self.use_xpos = use_xpos
        self.position_interpolation_scale = position_interpolation_scale
        self.transformer_engine = transformer_engine
        super().__init__(**kwargs)